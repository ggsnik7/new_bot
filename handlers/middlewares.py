from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Callable, Awaitable, Dict
from time import time
import logging

logger = logging.getLogger(__name__)

class TestMiddleware(BaseMiddleware):
    async def __call__(self, 
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:
        

        print('Мы в мидл вари')
        result = await handler(event, data)
        print('Выходим, из мидлвари')

        return result
    

class UpdateMiddleware(BaseMiddleware):
    async def __call__(self,
                       handeler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        
        start = time()
        result = await handeler(event, data)
        logger.debug(f'Время затраченное на опперацию: {time() - start}')

        return result


        

