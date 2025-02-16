class AgendadorDeTarefas:
    def __init__(self):
        self.heap = []

    def _pai(self, i):
        return (i - 1) // 2

    def _filho_esquerdo(self, i):
        return 2 * i + 1

    def _filho_direito(self, i):
        return 2 * i + 2

    def inserir_tarefa(self, tarefa, prioridade):
        self.heap.append((prioridade, tarefa))
        self._subir_heap(len(self.heap) - 1)

    def _subir_heap(self, i):
        while i > 0 and self.heap[i][0] < self.heap[self._pai(i)][0]:
            self.heap[i], self.heap[self._pai(i)] = self.heap[self._pai(i)], self.heap[i]
            i = self._pai(i)

    def remover_tarefa(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer_heap(0)
        return raiz

    def _descer_heap(self, i):
        menor = i
        esquerdo = self._filho_esquerdo(i)
        direito = self._filho_direito(i)

        if esquerdo < len(self.heap) and self.heap[esquerdo][0] < self.heap[menor][0]:
            menor = esquerdo
        if direito < len(self.heap) and self.heap[direito][0] < self.heap[menor][0]:
            menor = direito

        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._descer_heap(menor)

agendador = AgendadorDeTarefas()
agendador.inserir_tarefa('Tarefa A', 3)
agendador.inserir_tarefa('Tarefa B', 1)
agendador.inserir_tarefa('Tarefa C', 4)
agendador.inserir_tarefa('Tarefa D', 2)

print("Tarefa com maior prioridade:", agendador.remover_tarefa()[1])
print("Próxima tarefa:", agendador.remover_tarefa()[1])
