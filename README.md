#-----------------------------#
#          frontend           #
#-----------------------------#
# create python environement
	- python3 -m venv venv

# start python env
	- source venv/vin/activate

# install this library
	- pip install grpcio

# run the code
	- python client.py



#-----------------------------#
#          backend            #
#-----------------------------#
# create python environement
	- python3 -m venv venv

# start python env
	- source venv/vin/activate
	
# install these python libraries
	- pip install grpcio grpcio-tools pyfiglet

# goto asciiart folder and run the following command
	- python -m grpc_tools.protoc -I. --python_out=./asciiart --grpc_python_out=./asciiart asciiart.proto

# finally run the following command from the project root
	- python -m asciiart.server

