# bulk import to machine table, input specifies csv file
def import_machines(file):
    # import csv
    from app.models import Machine
    from app import db
    import os

    os.chdir('C:\\Users\\WDG1DCR\\Desktop\\my_projects\\web\\machine_data\\external')
    print('importing machine data...')
    entry_list = []
    with open(file, newline='') as csvfile:
        for row in csvfile:
            entry = (row.split(';'))
            entry_list.append(entry)
    for num in range(len(entry_list)):
        new_entry = Machine(project=entry_list[num][0],
                            prodline=entry_list[num][1],
                            serialnum=entry_list[num][2],
                            customer=entry_list[num][3],
                            description=entry_list[num][4])
        db.session.add(new_entry)
    db.session.commit()

# bulk import to kit table, input specifies csv file
def import_kits(file):
    from app.models import Kit
    from app import db
    import os

    os.chdir('C:\\Users\\WDG1DCR\\Desktop\\my_projects\\web\\machine_data\\external')
    print('importing kit data...')
    entry_list = []
    with open(file, newline='') as csvfile:
        for row in csvfile:
            entry = (row.split(';'))
            entry_list.append(entry)
    for num in range(len(entry_list)):
        new_entry = Kit(project=entry_list[num][0],
                            serialnum=entry_list[num][1],
                            customer=entry_list[num][2],
                            speed=entry_list[num][3],
                            length=entry_list[num][4],
                            width=entry_list[num][5],
                            depth=entry_list[num][6])
        db.session.add(new_entry)
    db.session.commit()

# delete everything from database
def nuke():
    from app.models import Machine, Kit
    from app import db

    print('nuking database...')
    machines = Machine.query.all()
    for m in machines:
        db.session.delete(m)
    kits = Kit.query.all()
    for k in kits:
        db.session.delete(k)
    db.session.commit()