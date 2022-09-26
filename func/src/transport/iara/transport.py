from iara_client import Iara, IaraTopics

from src.domain.exceptions.exceptions import ErrorSendingToIaraDatailCpfValidation


class BureauApiTransport:
    @staticmethod
    async def detail_transaction(unique_id: str):
        success, reason = await Iara.send_to_iara(
            topic=IaraTopics.CAF_SELFIE_VALIDATION_DETAILS,
            message={"unique_id": unique_id},
        )
        if not success:
            raise ErrorSendingToIaraDatailCpfValidation(str(reason))
        return True
