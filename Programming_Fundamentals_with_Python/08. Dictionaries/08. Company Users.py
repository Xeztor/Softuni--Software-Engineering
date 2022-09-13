data_companies = {}

company_user = input()
while 'End' not in company_user:
    comp_name, employee_id = company_user.split(' -> ')
    if comp_name not in data_companies:
        data_companies[comp_name] = [employee_id]
    else:
        if employee_id not in data_companies[comp_name]:
            data_companies[comp_name].append(employee_id)

    company_user = input()

data_companies = dict(sorted(data_companies.items(), key=lambda x: x[0]))

for comp_name, employee_ids in data_companies.items():
    print(f'{comp_name}')
    for employee_id in employee_ids:
        print(f'-- {employee_id}')
