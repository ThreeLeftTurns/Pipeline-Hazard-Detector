# Pipeline-Hazard-Detector

This program is capable of detecting pipelining hazards and generate a timing sequence chart based off of the provided traditional MIPS code operations. 

The code produces 3 solutions 
1) 'without any solution' which highlights registers and reports them to the console
   
2) 'with solution 1' which outputs the timing diagram following the F D X M W naming convention using only stalls to simulate the use of no forwarding unit 

3) 'with solution 2' which outputs the timing diagram following the same F D X M W convention with a forwarding unit enables.

this program includes basic mips instructions such as add, sub, lw, and sw. 
