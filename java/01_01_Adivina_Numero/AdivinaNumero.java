/*
 * Este programa adivina el numero, resultado final de una operación matematica
 *  El usuario introducira un numero como argumento, sin importar cual sea el numero el resultado, sera siempre
 *  el mismo
 *
 * @author: Alvaro Juanez M
 * @version: 1.0 - 25/01/2023
 *
 */
import java.util.Scanner;

public class AdivinaNumero{
    public static void main(String[] args){
        //Entrada de datos 
        Scanner scanner= new Scanner(args[0]); //Captura el argumento, lo guarda dentro de numPensado
        int numPensado = scanner.nextInt();    //Guarda un valor tipo int(Entero)
        int num;    //Realizara la operación matematica

        //Cerrando el Scanner para que no escanee nuevas lineas
        scanner.close();

        //Interactua con el usuario obtén los datos necesarios
        System.out.println("El numero Pensado es: " +  numPensado);

        //Multiplica por 3
        num = numPensado * 3;
        System.out.println("Si lo Multiplicas por 3: "  + num);

        //Sumale 6
        num = num + 6;
        System.out.println("Lo Sumas 6: " + num);

        //Dividelo entre 3
        num = num / 3;
        System.out.println("Lo Dividimos entre 6: " + num);

        //Le restamos con el numPensado
        num = num - numPensado;
        System.out.println("Si le restamos el valor inicial el resultado \ndeberia ser es 2");
        //Imprime el valor total de la operación matematica
        System.out.println("Resultado final es: " + num);
    }
}

