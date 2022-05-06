class Main {
    public static void main(String[] args) {
        System.out.printf("%s%n", "Hello World :D");
        System.out.printf("%s%n", "Hey all");
        System.out.printf("%s%n", "Hello World");

        System.out.printf("Number of args: %d%n", args.length);
    }

    public long calc() {
        long l = 0L;

        while(l < 10) {
            l += 1L;
        }

        return l;
    }
}