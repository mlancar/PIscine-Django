import settings

with open("myCV.template", "r", encoding="utf-8") as file:
    template = file.read()

data = {
    "desired_position": getattr(settings, "desired_position", ""),
    "name": getattr(settings, "name", ""),
    "age": getattr(settings, "age", ""),
    "address": getattr(settings, "address", ""),
    "phone_number": getattr(settings, "phone_number", ""),
    "email_address": getattr(settings, "email_address", ""),

    "image": getattr(settings, "image", ""),

    "time1": getattr(settings, "time1", ""),
    "job_name1": getattr(settings, "job_name1", ""),
    "job_description1": getattr(settings, "job_description1", ""),

    "time2": getattr(settings, "time2", ""),
    "job_name2": getattr(settings, "job_name2", ""),
    "job_description2": getattr(settings, "job_description2", ""),

    "time3": getattr(settings, "time3", ""),
    "job_name3": getattr(settings, "job_name3", ""),
    "job_description3": getattr(settings, "job_description3", ""),

    "time4": getattr(settings, "time4", ""),
    "job_name4": getattr(settings, "job_name4", ""),
    "job_description4": getattr(settings, "job_description4", ""),

    "school_name": getattr(settings, "school_name", ""),
    "school_name2": getattr(settings, "school_name2", ""),

    "hobby1": getattr(settings, "hobby1", ""),
    "hobby2": getattr(settings, "hobby2", ""),
    "hobby3": getattr(settings, "hobby3", ""),
    "hobby4": getattr(settings, "hobby4", "")
}

html = template.format(**data)

with open("cv.html", "w", encoding="utf-8") as file:
    file.write(html)