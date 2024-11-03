from app.dao.general_dao import GeneralDAO
from app.domain import Skill


class SkillsDAO(GeneralDAO):
    _domain_type = Skill


if __name__ == "main":
    # Код, який має виконатися при запуску модуля
    print("запущено")