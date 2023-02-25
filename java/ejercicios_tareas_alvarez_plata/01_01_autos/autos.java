/*Programa autos
 * El programa toma 2 valores enteros, los cuales en base a una operación matematica los convierte
 * a porcentaje de un total ya preestablecido en este caso 120 autos, para finalizar mostrara como resultado
 * el total de ambos porcentajes.
 * @author: Alvaro Juanez Mamani
 * @version: 1.0 23/02/2023
 * */

import java.util.Scanner;

public class autos{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);   //Entrada de datos

        //guarda la variables
        int porce1, porce2, total, total2;

        //Inicializa el programa
        System.out.println("los autos son 120");
        System.out.println("Cuanto de porcentaje son blancos? ");
        porce1 = scanner.nextInt();
        System.out.println("Cuanto de porcentaje son rojos? ");
        porce2 = scanner.nextInt();

        
        //cerrar el scanner
        scanner.close();
        
        //Realiza la operacion matematica
        total = (120 * porce1) / 100;
        total2 = (120 * porce2) / 100;
        
        //Muestra los resultados por pantalla
        System.out.println("El total de autos Blancos es:  " + total);
        System.out.println("El total de autos Rojos es:  " + total2);
        System.out.println("El restante son colores varios  " + (total = 120 - total - total2));
    }
}
