from . import jalali
from django.utils import timezone


def jalali_converter(miladi_time):
    list_of_months = ["فرورودین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن",
                      "اسفند"]
    miladi_time = timezone.localtime(miladi_time)

    time_to_str = f"{miladi_time.year}, {miladi_time.month}, {miladi_time.day}"
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(list_of_months):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    result = f"{time_to_list[2]} {time_to_list[1]} {time_to_list[0]} ساعت ,{miladi_time.hour}:{miladi_time.minute}"
    return result
