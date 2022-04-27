from cp import ContaPoupanca
from cc import ContaCorrente


cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(30)
cp.sacar(15)
cp.depositar(100)
cp.sacar(200)

print()

cc = ContaCorrente(3333, 4444, 0)
cc.depositar(10)
print(cc.limite)
cc.sacar(111)