import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Bienvenido a Bullshock Rullete Ai System Operanding");

        ArrayList<String> balas = new ArrayList<>();
         
        Scanner scanner = new Scanner(System.in);
        System.out.print("Balas Rojas / Negras (R/N): ");
        String inicio = scanner.nextLine();
        String[] parts = inicio.split(" ");
        Double rojas = Double.parseDouble(parts[0]);
        Double negras = Double.parseDouble(parts[1]);

        Double numeroX = rojas + negras;

        for (int i = 0; i < numeroX; i ++){
            balas.add("x");
        }

        System.out.println(balas);

        Boolean fin = false;

        do {
            Double total = rojas + negras;
            Scanner scanner2 = new Scanner(System.in);
            System.out.print("Telefono S/N: ");
            String telefono = scanner2.nextLine();

            if (telefono.equals("S")) {
                Scanner scanner3 = new Scanner(System.in);
                System.out.print("Posicion RN/x: ");
                String posicion = scanner3.nextLine();
                String[] posiciones = posicion.split(" ");
                String bala = posiciones[0];
                int lugar = Integer.parseInt(posiciones[1]);
                balas.set(lugar-1, bala);

                if (bala.equals("R") || bala.equals("r")){
                    rojas = rojas - 1;
                }
                if (bala.equals("N") || bala.equals("n")){
                    negras = negras -1;
                }
            }

            System.out.println(balas);

            if (balas.get(0).equals("R") || balas.get(0).equals("r")) {
                System.out.println("La probabilidad de morir es del 100 %.");
            }
            if (balas.get(0).equals("N") || balas.get(0).equals("n")) {
                System.out.println("La probabilidad de morir es del 0 %.");
            }
            if (balas.get(0).equals("x")) {
                Double probabilidad = rojas / total * 100;
                System.out.println(("La probabilidad de morir es del "+probabilidad+"%."));

                Scanner scanner4 = new Scanner(System.in);
                System.out.print("R/N: ");
                String disparo = scanner4.nextLine();
    
                if (disparo.equals("R") || disparo.equals("r")){
                    rojas = rojas - 1;
                }
                if (disparo.equals("N") || disparo.equals("n")){
                    negras = negras - 1;
                }
            }

            balas.remove(0);

            Scanner scanner5 = new Scanner(System.in);
            System.out.print("Has terminado la partida S/N: ");
            String finS = scanner5.nextLine();

            if (finS.equals("S") || balas.isEmpty()){
                fin = true;
            }

        } while (fin != true);

        System.out.println("Programa Finalizado! ^^");
        System.out.println("Mucha suerte en tu próxima rulera <3");
    }
}