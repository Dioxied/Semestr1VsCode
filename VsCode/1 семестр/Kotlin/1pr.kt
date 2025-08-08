fun main() {
    println("Введите номер задания, для выхода нажмите 0: ")
    var z : int= readLine()
    while (z != 0){
        if (z == 1){
            println("Введите число: ")
            var x1 = readLine()
            var x1kd = x1*x1
            var x1kb = x1*x1*x1
            print("Квадрат числа:  $x1kd , Куб числа:  $x1kb")
        }
    }
}