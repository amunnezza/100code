import os
print ("la directory su qui lavora python è " +  os.getcwd())
working_dir = os.path.realpath(os.path.dirname(__file__))
print ("mentre la directory in cui si trova il file è " + working_dir)
print ("per cambiare usa os.chdir(path)")
os.chdir(working_dir)
print ("infatti dopo avro che la directoty di lavoro è " + os.getcwd())