# Illumina-Attempt
Take Home assignment

# How to Run:
1. git pull this project into your directory locally. [git clone https://github.com/girdharJiten/Illumina-Attempt.git]
2. Make sure you have python3 installed, otherewise follow https://www.python.org/downloads/ and install latest version if python3.
3. If you have VScode installed you can open the Illumina-Attempt folder in it and go to logProcessor.py file, else you can go to terminal and got Illumina-Attempt folder which has all the code and data files.
4. if you have VScode you can go to logProcessor.py and click on the run button on the top right corner of the screen which should generate a output.txt file with outputs of first 3 cases and your console should show error message pertaining to fourth case.
5. If you are running from commandline you can run [python3 logProcessor.py] in the terminal which should execute the program and process those files.

In this assignment i created sample log data of 2 types to demo how the code will handle default log and custom log structure and how it affects our log processing.

# Assumptions:
1. I assume that look up table is not going to change formatting wise.
2. I assume that tags are based on lookup table and so are the port/protocol combination, which means only those logs which can be tagged will be part of the port/protocol mapping.
3. User should know if their log format is custom. If it is custom format then user should enter, protocol_index and dstport_index so that we can tag logs. There are some safety statements in the code which means that the code will not print anything and let you know that there is an issue with your code. If your indices are wrong then you will see all logs being "Untagged" and zero port/protocol combinations. More explaination in the highlights section.
4. According to file size requirements given, both the files can be stored in ram of any computer.
5. lookup.csv and sampleData.txt are assumed formats of data copied from the email.
6. Program only focuses on version 2 logs.

# Highlights:
1. The program can process defaultlogs with just log location, but for custom logs user needs to add some attributs of log data.
2. We add support for custom logs, but user should know the indices of protocol and dstport, otherwise counters will not work properly.
3. Program runs 3 types of log formats:
    1. first is default log format which processes data in the way shown in the email where we know the appropriate indices.
        Output has correct number of tags and their counters. Output in printed in output.txt
    2. Second is customer format but user knows appropriate indices
        Output has correct number of tags and their counters. Output in printed in output.txt
    3. Third is another custom format but user inputs wrong index data
        Output has incorrect tagging and zero port/protocol counters as all logs are Untagged. But is still prints something on the file.
    4. Fourth custom format with information wrong
        You get a message form program informing you to enter correct indices and try again.
4. We can extend the Logprocessor class to do other types of processing by adding new methods in the class.

# Limitations:
1. In this format progarm only evaluates logs based on indices which might break due to user inputing wrong index. We can improve code readability by using advanced libraries like pandas which provide support for checking if data has certain columns by name which is more explainable to a new user.
2. Current structure of code is written to mostly do one thing. Over time as things get more complicated we would want to separate parts of tagging logs, generating custom counter and writing counters to output file.

# Extension:
1. If size of logs increase such that they can no longer be kept in RAM then we can update our code to use Big Data tools like Spark.
2. As logs accumulate and size increases we can use these counters to create some levels to let developers know if there is a problem. ex: if there is a mapping issue w,r.t log statements such that protocol index doesn't allign with what we had before then these counters can let developers know so they can look into this issue.
3. If we want to store log formats we can create a log data structure which can store data like protocl_index, dstprt_index and maxColNames and can directly be used to initialize LogProcessor.

class LogConfig:
    filePath: str = "sampleData.txt"
    isDefaultFormat: bool = True
    protocolIndex: int = 7
    dstPortIndex: int = 6
    columnNumber: int = 14





