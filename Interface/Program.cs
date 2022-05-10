using System;
using System.Diagnostics;

string filename = "/usr/bin/sudo"; //path with commands
string command = "python ../Lock_Control/lock.py"; //run the command to execute the script
Process commandExec = new Process();
commandExec.StartInfo.FileName = filename;
commandExec.StartInfo.Arguments = command;
commandExec.StartInfo.UseShellExecute = true; //tells the process to call a  command
commandExec.Start();
