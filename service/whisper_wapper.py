import openai
from backoff import on_exception, expo
from io import BytesIO
from typing import Optional
import concurrent.futures
import asyncio
import traceback
from loguru import logger
from errors import Errors

async def process_audio(audio, timeout, model="whisper-1"):
    try:
        params = dict(
            model=model,
            file=audio,
            request_timeout=timeout,
        )

        transcript = await _create_async(params)
        if transcript is None:
            yield Errors.SOMETHING_WRONG_IN_OPENAI_WHISPER_API.value
            return

        prompt = transcript["text"]
        logger.debug("audio prompt: {}".format(prompt))
        del audio
    except:
        err = traceback.format_exc()
        logger.error(err)
        yield Errors.SOMETHING_WRONG.value
        return

    if not prompt:
        yield Errors.PROMPT_IS_EMPTY.value
        return

    yield "data: " + prompt


@on_exception(expo, openai.error.RateLimitError, max_tries=5)
def _create(params):
    return openai.Audio.transcribe(**params)


async def _create_async(params):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        try:
            result = await asyncio.get_event_loop().run_in_executor(
                executor, _create, params
            )
        except:
            err = traceback.format_exc()
            logger.error(err)
            # 这里处理 openai.error.RateLimitError 之外的错误
            return None
    return result
