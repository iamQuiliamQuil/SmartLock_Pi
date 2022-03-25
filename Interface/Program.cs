using System;
using System.Diagnostics;

string filename = "/usr/bin/sudo";
string command = "python ../Lock_Control/lock.py";
Process commandExec = new Process();
commandExec.StartInfo.FileName = filename;
commandExec.StartInfo.Arguments = command;
commandExec.StartInfo.UseShellExecute = true;
commandExec.Start();
