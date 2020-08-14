from datetime import datetime, timedelta

def rename(previous_name: str) -> str:
    name_list = previous_name.split('.')

    now = datetime.utcnow() - timedelta(hours=7)
    name_list[-2] += f"-{now.strftime(r'%Y-%m-%d')}"

    return '.'.join(name_list)
