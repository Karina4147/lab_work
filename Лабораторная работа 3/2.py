# TODO Напишите функцию find_common_participants
def find_common_participants(participant_first: str, participant_second: str, name=","):
    participant_first_1 = participant_first.split(name)
    participant_second_2 = participant_second.split(name)
    common_list = list(set(participant_first_1).intersection((set(participant_second_2))))
    common_list.sort()
    return common_list
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, name='|'))


# TODO Проверьте работу функции с разделителем отличным от запятой
