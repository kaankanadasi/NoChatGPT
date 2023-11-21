public class Dog {
    /* 
    !!!
    !!!!!!
    kod için herhangi büyük bir yardım takviyesi (AI tools, google, kami vb.) kullanılmamıştır, commentların bazılarında 
    google, chatgpt'den yardım alınmıştır, kodda sadece çok küçük değişiklikler için yapay zeka kullanılmıştır, saygılar Kaan Kanadaşı 
    !!!!!!
    !!!
    */ 

    private String name;
    private String breed;
    private int age;
    /* Class attributes are variables defined in the class. These attributes define the state of 
    the object at a particular time. Variables that belong to an object are called attributes */ 

    public Dog() {}
    // default value for Dog

    public Dog(String name, String breed, int age) {
    // constructor and signature 
        this.name = name;
        this.breed = breed;
        this.age = age;
        // initializing the attributes - to set the initial state of an object when it is created
    }

    // String, String ve int yazmayı unuttum - chatgpt yardımı
    // birşey return ediyorsak o şeyin type'ını yazmamız lazım - storege da ne kadar yer kaplayacağını anlasın diye herhalde
    public String getName() {
        return name;
    }
    public String getBreed() {
        return breed;
    }
    public int getAge() {
        return age;
    }
    
    /* allows as to change parameters on the objects that we create - en azından ben böyle anladım */ 
    // void yazmayı unuttum - chatgpt yardımı - meğerse eğer bir şey return etmiyorsak void yazıyormuşuz 
    public void setName(String name) {
        this.name = name;
    }
    public void setBreed(String breed) {
        this.breed = breed;
    }
    public void setAge(int age) {
        this.age = age;
    }
    /* When you are creating setter methods in your class, you typically want them to modify the object's internal 
    state (instance variables) without returning any value, which is why you specify void as the return type. */ 

    public String toString() 
        // bunu neden kullandığımızı anlamadım ama "name", "breed" ve "age" variable'larının hepsini stringe çeviriyor 
        // - public static void main(String[] args) de kullanabilirdik sanki - void kullanılmamış String kullanılmış neden return var
    {
        return "The name of the dog is " + name + ". The breed of the dog is " + breed + ". The age of the dog is " + age + ".";
    }

    public static void main(String[] args) {
        // return yok o yüzden void kullanılmış
        Dog doggo = new Dog("Kaan", "human", 18);
        // creating a new object doggo
        Dog deafault = new Dog();
        // creating a new object deafault
        System.out.println(doggo);

        boolean result = doggo.equals(deafault);     
        if (result) {
            System.out.println("The default dog is equal to the new dog");
        } else {
            System.out.println("The default dog is not equal to the new dog");
        }
        
    }
}