import sys
if len(sys.argv) == 2 :
	n = int(sys.argv[1])
else :
	n = 10
mod = "mod EXAMPLE is inc DeltaCCS .\n"
mod = mod + "op Proc : -> DeltaCCSProcess .\n"
context = "eq context =  "
L = ""
Proc = ""
for i in range(n):
	p = "\'Phil" + str(i)
	context += "\n( " + p + " =def "
	context += "\'think . "+ p
	context += " + ~ \'up" +str(i) + " . ~ \'up" +str((i + 1)%n) + " . \'eat"
	context += " . ~ \'dn" + str(i) + " . ~ \'dn" + str((i + 1)%n) + " . " + p
	context += " ) &"
	f = "\'Fork" +str(i)
	context += "\n( " + f + " =def "
	context += "\'up" + str(i) + " . \'dn" + str(i) + " . " + f
	context += " ) &"
	L = L + " \ \'up" + str(i) + " \ \'dn" + str(i)
	if i == 0 :
		Proc += "( " + p +" | " + f + " )"
	else :
		Proc = "( ( " + Proc + " | " + p + " )" + " | " + f + " )"
context = context[0:-1] + "."
mod += "\n\n" + context
mod += "\n\n"
mod += "eq deltaSet = empty ."
mod += "\n\n"
mod += "eq Proc = ( ( " + Proc + L + "), empty ) ."
mod += "\n\n"
mod += "endm"
mod += "\n\n\n"
mod += "red in mu-calculus : {} {} 'Proc.DeltaCCSProcess |= Nu X [-]X /\ <-># SVA # SVA ."
fobj = open("philo"+str(n)+".maude", "w")
fobj.write(mod)
fobj.close()


