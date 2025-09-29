 **Registers and instructions in Assembly**: I noticed that registers are the fastest storage locations in the CPU, and instructions usually operate directly on them instead of slower memory. Each register has a specific role, like holding data, addresses, or intermediate results. Instructions are simple and precise, telling the CPU exactly what operation to perform. The efficiency of a program often depends on how well registers are used. Overall, registers and instructions work closely together to speed up processing.

**Coding in Assembly**: Coding in assembly is pretty much complex as compared to pyhton. Codes in Pyhton are short and easy to write, it can be termed as programmer friendly . On the other hand, Assembly language requires a long code even for simple addition. It is computer friendly but far from human languages.

**Why is python faster?** Python is faster for writing codes bacause it is a growing high level language. Its codes are short,comprehensive and precise. Moreover, it provides functions, loops and conditions to write any type of program with complex requiremnets. Python also provides rich libraries and supports multiple paradigms like OOP and functional programming.

**Abstraction in Python**:Abstraction in Python is mainly supported through **classes and abstract classes**. By using the `abc` (Abstract Base Class) module, we can define abstract methods that only provide a blueprint, leaving the actual implementation to child classes. This way, a programmer can hide unnecessary details and only show the essential features. For example, you can define a general "Vehicle" class without worrying about how each vehicle type works internally. It makes code cleaner, more organized, and easier to extend. In simple words, abstraction in Python helps us focus on what a thing does rather than how it does it.

###  Comparison Table

| Feature          | Assembly Example | Python Example | Notes                                           |
|------------------|------------------|----------------|------------------------------------------------|
| Variable storage | Register (EAX)   | `x = 7`        | In assembly, values are stored in CPU registers; in Python, variables handle storage automatically. |
| Printing output  | `INT 21h`        | `print()`      | Assembly requires system interrupts, while Python has a built-in simple function. |
| Arithmetic       | `ADD AX, BX`     | `x + y`        | Assembly operates on registers directly, while Python uses operators with variables. |

