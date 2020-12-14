
import java.util.Calendar;

 // älä muuta !
public class DIPTehtava {

    private static BusinessLuokka businessLuokkaAutolle = DIPConfigurator.konfiguraatioAutolle();

    private static BusinessLuokka businessLuokkaMoottoripyoralle = DIPConfigurator.konfiguraatioMoottoripyorille();

    public static void main(final String[] args) {
        System.out.println("Järjestelmän autolla on " + "ajettu keskimäärin vuodessa: "
                + businessLuokkaAutolle.laskeKeskimaaraisetKilometritPerVuosi() + " kilometriä");

        System.out.println("Järjestelmän moottoripyörälla on " + "ajettu keskimäärin vuodessa: "
                + businessLuokkaMoottoripyoralle.laskeKeskimaaraisetKilometritPerVuosi() + " kilometriä");
    }
}

// ---------------------------------------------------------------------------------------------------------------------
// muokattavaa
class DIPConfigurator {

    public static BusinessLuokka konfiguraatioAutolle() {
        final BusinessLuokka businessLuokkaAutolle = new BusinessLuokka();
	// täällä konfoguroidaan auto (new)
        Auto auto = new Auto(5000, 2010, true);
	// asetetaan ajoneuvoksi set metodilla
        businessLuokkaAutolle.setAjoneuvo(auto);
        return businessLuokkaAutolle;
    }

    public static BusinessLuokka konfiguraatioMoottoripyorille() {
        final BusinessLuokka businessLuokkaMoottoripyoralle = new BusinessLuokka();
	// täällä konfoguroidaan moottipyora (new)
        Moottoripyora moottoripyora = new Moottoripyora(77000,2012,false);
	// asetetaan ajoneuvoksi set metodilla
        businessLuokkaMoottoripyoralle.setAjoneuvo(moottoripyora);
        return businessLuokkaMoottoripyoralle;
    }
}


// ---------------------------------------------------------------------------------------------------------------------
// rajapinta
interface Ajoneuvo {
    public int getAjetutKilometrit();

    public int getVuosimalli();
}


// ---------------------------------------------------------------------------------------------------------------------
// auto luokka, joka toteuttaa ajoneuvo rajapintaa
class Auto implements Ajoneuvo {
    private final int km;
    private final int vuosimalli;
    private final boolean onkoFarmari;

    public Auto(final int km, final int vuosimalli, final boolean onkoFarmari) {
        this.km = km;
        this.vuosimalli = vuosimalli;
        this.onkoFarmari = onkoFarmari;
    }

    public int getAjetutKilometrit() {
        return this.km;
    }

    public int getVuosimalli() {
        return this.vuosimalli;
    }

    public boolean onkoFarmari() {
        return this.onkoFarmari;
    }
}


// ---------------------------------------------------------------------------------------------------------------------
// moottoripyora luokka, joka toteuttaa ajoneuvo rajapintaa
class Moottoripyora implements Ajoneuvo {
    private final int km;
    private final int vuosimalli;
    private final boolean onkoKevytMoottoripyora;

    public Moottoripyora(final int km, final int vuosimalli, final boolean onkoKevytMoottoripyora) {
        this.km = km;
        this.vuosimalli = vuosimalli;
        this.onkoKevytMoottoripyora = onkoKevytMoottoripyora;
    }

    public int getAjetutKilometrit() {
        return km;
    }

    public int getVuosimalli() {
        return vuosimalli;
    }

    public boolean onkoKevytMoottoripyora() {
        return this.onkoKevytMoottoripyora;
    }
}


// ---------------------------------------------------------------------------------------------------------------------
// BusinessLuokka
class BusinessLuokka {
   
    // nyt business luokka voi käsitellä järjestelmän erilaisia ajoneuvoja
    Ajoneuvo ajoneuvo;	
	
    public int laskeKeskimaaraisetKilometritPerVuosi() {
        return ajoneuvo.getAjetutKilometrit() / ((Calendar.getInstance().get(Calendar.YEAR) - ajoneuvo.getVuosimalli()) + 1);
    }

   
    public void setAjoneuvo(final Ajoneuvo ajoneuvo) {
	// set metodi asettaa käsiteltävän ajoneuvo rajapinnan ilmentymän (auto / moottoripyora -olio)
	this.ajoneuvo = ajoneuvo;
    }
}