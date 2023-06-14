# test : arduino.o user.o
# 	clang arduino.o user.o -o test

# arduino.o : arduino.c arduino.h
# 	clang -c -o arduino.o arduino.c

# user.o : user.c arduino.h
# 	clang -c -o user.o user.c

# clean:
# 	rm *.o test

# arduino_compiled : arduino.o user.o
# 	arm-linux-gnueabihf-gcc -static -o arduino_compiled arduino.o user.o

# arduino.o : arduino.c arduino.h
# 	arm-linux-gnueabihf-gcc -static -c -o arduino.o arduino.c

# user.o : user.c arduino.h
# 	arm-linux-gnueabihf-gcc -static -c -o user.o user.c

# clean :
# 	rm *.o arduino_compiled

arduino_none_compiled : arduino.o user.o
	arm-none-eabi-gcc --specs=nosys.specs -static -o arduino_none_compiled arduino.o user.o

arduino.o : arduino.c arduino.h
	arm-none-eabi-gcc --specs=nosys.specs -static -c -o arduino.o arduino.c

user.o : user.c arduino.h
	arm-none-eabi-gcc --specs=nosys.specs -static -c -o user.o user.c

clean :
	rm *.o arduino_none_compiled
