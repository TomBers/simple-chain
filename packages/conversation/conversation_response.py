content = (
    """
    <div hx-swap-oob="{ordering}:#{div_id}">
        {data}
    </div>
    """
)

# res = {'input': 'Tell me about RAM', 'history': 'Human: Good morning AI!\nAI: Good morning! How can I assist you today?\nHuman: I want to know about memory\nAI: Memory is the ability of an organism to encode, store, retain, and retrieve information. It plays a crucial role in our daily lives, allowing us to learn, make decisions, and remember past experiences. In the context of computers, memory refers to the electronic components used to store and retrieve data. This can include both temporary storage, such as random access memory (RAM), and long-term storage, such as hard disk drives or solid-state drives. Is there something specific you would like to know about memory?',
#        'response': "RAM, or random access memory, is a type of computer memory that is used for temporary storage of data that is actively being manipulated or accessed by the computer's CPU. It is a volatile memory, meaning that its contents are lost when the computer is powered off or restarted. RAM is an essential component of a computer system as it provides the CPU with fast access to data that is needed for current tasks.\n\nRAM is organized into small, fixed-size storage units called memory cells. Each memory cell is capable of storing a single bit of information, which can be either a 0 or a 1. These bits are grouped together to form bytes, with each byte typically consisting of 8 bits. The capacity of RAM is measured in bytes, with common sizes ranging from a few gigabytes (GB) to several terabytes (TB) in modern computers.\n\nThe speed of RAM is another important characteristic. It is typically measured in megahertz (MHz) or gigahertz (GHz), and it determines how quickly data can be read from or written to the memory. Faster RAM can improve overall system performance by reducing the time it takes for the CPU to access data.\n\nThere are different types of RAM, including dynamic random access memory (DRAM) and static random access memory (SRAM). DRAM is the most common type of RAM used in personal computers and is characterized by its higher storage density and lower cost. SRAM, on the other hand, is faster and more expensive, but it is used in specialized applications where speed is critical, such as cache memory.\n\nIn summary, RAM is a crucial component of a computer system that provides temporary storage for actively used data. It allows the CPU to quickly access and manipulate data, resulting in faster and more efficient computing."}

# prev_res = "Human: Good morning AI!\nAI: Good morning! How can I assist you today?\n"

first_res = {'input': 'good morning', 'history': '',
             'response': "Good morning! Did you know that the average morning temperature in this area is 68 degrees Fahrenheit? It's a great time to start the day!"}

second_res = {'input': 'Can you tell me about RAM', 'history': "Human: good morning\nAI: Good morning! Did you know that the average morning temperature in this area is 68 degrees Fahrenheit? It's a great time to start the day!",
              'response': 'RAM stands for Random Access Memory. It is a type of computer memory that can be accessed randomly, meaning any byte of memory can be accessed without touching the preceding bytes. It is used to store data and machine code currently being used. The speed and efficiency of RAM greatly affects the overall performance of a computer. It is different from a hard drive, which stores data for the long term. Do you want to know more about its technical specifications or its uses in computer systems?'}

third_res = {'input': 'Third question', 'history': "Human: good morning\nAI: Good morning! Did you know that the average morning temperature in this area is 68 degrees Fahrenheit? It's a great time to start the day!\nHuman: Can you tell me about RAM\nAI: RAM stands for Random Access Memory. It is a type of computer memory that can be accessed randomly, meaning any byte of memory can be accessed without touching the preceding bytes. It is used to store data and machine code currently being used. The speed and efficiency of RAM greatly affects the overall performance of a computer. It is different from a hard drive, which stores data for the long term. Do you want to know more about its technical specifications or its uses in computer systems?",
             'response': 'Third response'}

example_responses = [first_res, second_res, third_res]


def test_response(res, div_id="content"):

    output = "<div class='message human'>{}</div><div class='message ai'>{}</div>".format(res.get(
        'input', ''), res.get('response', ''))

    return content.format(data=output, div_id=div_id, ordering="beforeend")


def conversation_response(data, div_id="content", from_top=False):
    ordering = "afterbegin" if from_top else "beforeend"
    return content.format(data=data, div_id=div_id, ordering=ordering)
