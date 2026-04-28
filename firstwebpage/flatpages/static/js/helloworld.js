var groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БФИ2404",
        "marks": [2,3,5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1701",
        "marks": [5,4,5]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БВТ1502",
        "marks": [5,3,3]
    }
];

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
}

var sredniyBal = function(marks) {
    bal = 0;
    for (var i = 0; i < marks.length; i++){
        bal += marks[i];
    }
    bal /= marks.length;
    return bal;
}

var printStudents = function(students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i <= students.length-1; i++){
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
}

var printStudentsGroup = function(students, filter) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i <= students.length-1; i++){
        if (filter == null || students[i]['group'] == filter){
            console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
            );
        }
    }
    console.log('\n');
}

var printStudentsSredniy = function(students, filter) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20),
        rpad("Средний бал", 10),
    );
    for (var i = 0; i <= students.length-1; i++){
        if (filter == null || sredniyBal(students[i]['marks']) > filter){
            console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20),
            rpad(sredniyBal(students[i]['marks']), 20)
            );
        }
    }
    console.log('\n');
}

printStudents(groupmates);