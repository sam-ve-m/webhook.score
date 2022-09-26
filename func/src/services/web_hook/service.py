import asyncio

from src.domain.validator.webhook.validator import WebHookMessage
from src.repositories.bureau_transactions.repository import BureauTransactionRepository
from src.repositories.user.repository import UserRepository
from src.transport.iara.transport import BureauApiTransport
from src.transport.persephone.transport import SendToPersephone


class BureauValidationService:
    @classmethod
    async def save_bureau_validation(cls, webhook_message: WebHookMessage) -> bool:
        unique_id = await BureauTransactionRepository.get_user_unique_id_of_transaction(webhook_message)
        await SendToPersephone.register_user_cpf_validation_log(unique_id, webhook_message)
        update_transaction = BureauTransactionRepository.update_bureau_transaction(webhook_message)
        send_to_iara = BureauApiTransport.detail_transaction(unique_id)
        update_user = UserRepository.update_bureau_validation(unique_id, webhook_message)
        success = all(await asyncio.gather(
            update_user, update_transaction, send_to_iara
        ))
        return success
