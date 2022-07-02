Transofrm orchive from format of

```bash
submits
├── Акимов Сергей Вадимович-98418754
│   ├── A-67430420-gcc_cpp20-WrongAnswer.cpp
│   ├── A-67430541-gcc_cpp20-WrongAnswer.cpp
│   ├── A-67430579-gcc_cpp20-WrongAnswer.cpp
│   ├── A-67430656-gcc_cpp20-OK.cpp
│   ├── B-67430777-gcc_cpp20-OK.cpp
│   ├── C-67432084-gcc_cpp20-WrongAnswer.cpp
│   ├── C-67432566-gcc_cpp20-OK.cpp
├── Яндулов Богдан Сергеевич-98418851
│   ├── A-67423003-gcc_cpp20-OK.cpp
│   ├── B-67422735-gcc_cpp20-OK.cpp
│   └── C-67422683-gcc_cpp20-OK.cpp
└── Ящинская Елизавета Дмитриевна-98418852
    ├── A-67470568-gcc7_3-OK.cpp
    ├── B-67470966-gcc7_3-WrongAnswer.cpp
    ├── B-68168461-gcc7_3-OK.cpp
    ├── B-68204892-gcc7_3-WrongAnswer.cpp
    ├── B-68205187-gcc7_3-OK.cpp
    ├── C-68204315-gcc7_3-WrongAnswer.cpp
    ├── C-68204338-gcc7_3-WrongAnswer.cpp
    ├── C-68204532-gcc7_3-PresentationError.cpp
    ├── C-68204541-gcc7_3-WrongAnswer.cpp
    ├── C-68204643-gcc7_3-RuntimeError.cpp
    └── C-68204690-gcc7_3-WrongAnswer.cpp
```

into one of format
```
submits
├── A
│   ├── A-67430656-gcc_cpp20-OK.cpp
|   ├── A-67423003-gcc_cpp20-OK.cpp
│   └── A-67470568-gcc7_3-OK.cpp
├── B
│   ├── B-67430777-gcc_cpp20-OK.cpp
│   ├── B-67422735-gcc_cpp20-OK.cpp
│   └── B-68168461-gcc7_3-OK.cpp
└── C
    ├── C-67432566-gcc_cpp20-OK.cpp
    └── C-67422683-gcc_cpp20-OK.cpp
```
leaving ot most 1 OK submission from each participant