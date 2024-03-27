def solution(today, terms, privacies):
    answer = []
    today_year, today_month, today_day = map(int,today.split('.'))
    terms_dict = {}
    for term in terms:
        name, month = term.split()
        terms_dict[name] = int(month) * 28
        
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        year, month, day = map(int,date.split('.'))
        year_diff = (today_year - year) * (12 * 28)
        month_diff = (today_month - month) * 28
        day_diff = (today_day - day)
        total_diff = year_diff + month_diff + day_diff
        if terms_dict[term] <= total_diff:
            answer.append(i+1)
    return answer