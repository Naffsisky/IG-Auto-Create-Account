import string
import random


# Generating name functions 
# You can create different surnames to increase the variety of usernames.
def generatingName():
    firstName = ["Alan", "Murat", "Azad", "Necati", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan",
                 "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
                 "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed",
                 "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel",
                 "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam",
                 "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil",
                 "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed",
                 "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian",
                 "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay",
                 "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert",
                 "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs",
                 "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf",
                 "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider",
                 "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen",
                 "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan",
                 "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer",
                 "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs",
                 "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet",
                 "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio",
                 "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep",
                 "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez",
                 "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis",
                 "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran",
                 "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved",
                 "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley",
                 "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal",
                 "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun",
                 "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan",
                 "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub",
                 "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise",
                 "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley",
                 "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz",
                 "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz",
                 "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay",
                 "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod",
                 "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue",
                 "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony",
                 "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly",
                 "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee",
                 "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan",
                 "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody",
                 "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan",
                 "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak",
                 "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan",
                 "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Melim"]

    surName = ["Abak", "Demir", "Bala", "yilmaz", "Ediz",
               "yasar", "Ozbal", "Aydin", "kara",
               "Bakar", "Zengin", "Bilgin", "Kilic",
               "karabulut", "Abbas", "Hammoud", "Alan",
               "tilki", "Aslan", "Boz", "karaeski",
               "Deniz", "Temiz", "Alpaslan", "Demirci",
               "Erol", "Guneri", "yasin", "yelken",
               "Elmas", "Altin", "guller", "Bagci",
               "yucel", "korkmaz", "cetin","Dari",
               "Albayrak", "Tekin", "Yurtkulu", "Metin",
               "Suvari", "Kizilay", "Inan", "tasi", "Akdeniz",
               "Albagu", "alk", "Acu", "Altun", "Karagul",
               "Avkar", "Ayana", "Alagan", "Akar"]
    return ''.join(random.choice(firstName) + ' ' + random.choice(surName))


# Generating a username
def username(size=8, chars=string.ascii_lowercase + random.choice(['.', '_'])):
    word_list = [
        "pulpenpilott", "bengbengkeju", "nuenaonwe", "pantogoreng", "panoncoklats", "Agus99", "Asepjalamsx", "Adindadsxz", "Putrimnchz", "Steventhreenxz", 
        "Dadadangg", "Kevinnod", "Mutiarasx", "Clarafrz",
        "pulpenpilott0","pulpenpilott1","pulpenpilott2","pulpenpilott3","pulpenpilott4","pulpenpilott5","pulpenpilott6","pulpenpilott7","pulpenpilott8","pulpenpilott9","pulpenpilott10","pulpenpilott11","pulpenpilott12","pulpenpilott13","pulpenpilott14","pulpenpilott15","pulpenpilott16","pulpenpilott17","pulpenpilott18","pulpenpilott19","pulpenpilott20","pulpenpilott21","pulpenpilott22","pulpenpilott23","pulpenpilott24","pulpenpilott25","pulpenpilott26","pulpenpilott27","pulpenpilott28","pulpenpilott29","pulpenpilott30","pulpenpilott31","pulpenpilott32","pulpenpilott33","pulpenpilott34","pulpenpilott35","pulpenpilott36","pulpenpilott37","pulpenpilott38","pulpenpilott39","pulpenpilott40","pulpenpilott41","pulpenpilott42","pulpenpilott43","pulpenpilott44","pulpenpilott45","pulpenpilott46","pulpenpilott47","pulpenpilott48","pulpenpilott49","pulpenpilott50","pulpenpilott51","pulpenpilott52","pulpenpilott53","pulpenpilott54","pulpenpilott55","pulpenpilott56","pulpenpilott57","pulpenpilott58","pulpenpilott59","pulpenpilott60","pulpenpilott61","pulpenpilott62","pulpenpilott63","pulpenpilott64","pulpenpilott65","pulpenpilott66","pulpenpilott67","pulpenpilott68","pulpenpilott69","pulpenpilott70","pulpenpilott71","pulpenpilott72","pulpenpilott73","pulpenpilott74","pulpenpilott75","pulpenpilott76","pulpenpilott77","pulpenpilott78","pulpenpilott79","pulpenpilott80","pulpenpilott81","pulpenpilott82","pulpenpilott83","pulpenpilott84","pulpenpilott85","pulpenpilott86","pulpenpilott87","pulpenpilott88","pulpenpilott89","pulpenpilott90","pulpenpilott91","pulpenpilott92","pulpenpilott93","pulpenpilott94","pulpenpilott95","pulpenpilott96","pulpenpilott97","pulpenpilott98","pulpenpilott99","pulpenpilott100",
        "nuedanleupas0","nuedanleupas1","nuedanleupas2","nuedanleupas3","nuedanleupas4","nuedanleupas5","nuedanleupas6","nuedanleupas7","nuedanleupas8","nuedanleupas9","nuedanleupas10","nuedanleupas11","nuedanleupas12","nuedanleupas13","nuedanleupas14","nuedanleupas15","nuedanleupas16","nuedanleupas17","nuedanleupas18","nuedanleupas19","nuedanleupas20","nuedanleupas21","nuedanleupas22","nuedanleupas23","nuedanleupas24","nuedanleupas25","nuedanleupas26","nuedanleupas27","nuedanleupas28","nuedanleupas29","nuedanleupas30","nuedanleupas31","nuedanleupas32","nuedanleupas33","nuedanleupas34","nuedanleupas35","nuedanleupas36","nuedanleupas37","nuedanleupas38","nuedanleupas39","nuedanleupas40","nuedanleupas41","nuedanleupas42","nuedanleupas43","nuedanleupas44","nuedanleupas45","nuedanleupas46","nuedanleupas47","nuedanleupas48","nuedanleupas49","nuedanleupas50","nuedanleupas51","nuedanleupas52","nuedanleupas53","nuedanleupas54","nuedanleupas55","nuedanleupas56","nuedanleupas57","nuedanleupas58","nuedanleupas59","nuedanleupas60","nuedanleupas61","nuedanleupas62","nuedanleupas63","nuedanleupas64","nuedanleupas65","nuedanleupas66","nuedanleupas67","nuedanleupas68","nuedanleupas69","nuedanleupas70","nuedanleupas71","nuedanleupas72","nuedanleupas73","nuedanleupas74","nuedanleupas75","nuedanleupas76","nuedanleupas77","nuedanleupas78","nuedanleupas79","nuedanleupas80","nuedanleupas81","nuedanleupas82","nuedanleupas83","nuedanleupas84","nuedanleupas85","nuedanleupas86","nuedanleupas87","nuedanleupas88","nuedanleupas89","nuedanleupas90","nuedanleupas91","nuedanleupas92","nuedanleupas93","nuedanleupas94","nuedanleupas95","nuedanleupas96","nuedanleupas97","nuedanleupas98","nuedanleupas99","nuedanleupas100",
        "nuenaonwe0","nuenaonwe1","nuenaonwe2","nuenaonwe3","nuenaonwe4","nuenaonwe5","nuenaonwe6","nuenaonwe7","nuenaonwe8","nuenaonwe9","nuenaonwe10","nuenaonwe11","nuenaonwe12","nuenaonwe13","nuenaonwe14","nuenaonwe15","nuenaonwe16","nuenaonwe17","nuenaonwe18","nuenaonwe19","nuenaonwe20","nuenaonwe21","nuenaonwe22","nuenaonwe23","nuenaonwe24","nuenaonwe25","nuenaonwe26","nuenaonwe27","nuenaonwe28","nuenaonwe29","nuenaonwe30","nuenaonwe31","nuenaonwe32","nuenaonwe33","nuenaonwe34","nuenaonwe35","nuenaonwe36","nuenaonwe37","nuenaonwe38","nuenaonwe39","nuenaonwe40","nuenaonwe41","nuenaonwe42","nuenaonwe43","nuenaonwe44","nuenaonwe45","nuenaonwe46","nuenaonwe47","nuenaonwe48","nuenaonwe49","nuenaonwe50","nuenaonwe51","nuenaonwe52","nuenaonwe53","nuenaonwe54","nuenaonwe55","nuenaonwe56","nuenaonwe57","nuenaonwe58","nuenaonwe59","nuenaonwe60","nuenaonwe61","nuenaonwe62","nuenaonwe63","nuenaonwe64","nuenaonwe65","nuenaonwe66","nuenaonwe67","nuenaonwe68","nuenaonwe69","nuenaonwe70","nuenaonwe71","nuenaonwe72","nuenaonwe73","nuenaonwe74","nuenaonwe75","nuenaonwe76","nuenaonwe77","nuenaonwe78","nuenaonwe79","nuenaonwe80","nuenaonwe81","nuenaonwe82","nuenaonwe83","nuenaonwe84","nuenaonwe85","nuenaonwe86","nuenaonwe87","nuenaonwe88","nuenaonwe89","nuenaonwe90","nuenaonwe91","nuenaonwe92","nuenaonwe93","nuenaonwe94","nuenaonwe95","nuenaonwe96","nuenaonwe97","nuenaonwe98","nuenaonwe99","nuenaonwe100",
        "tjlsdhea0","tjlsdhea1","tjlsdhea2","tjlsdhea3","tjlsdhea4","tjlsdhea5","tjlsdhea6","tjlsdhea7","tjlsdhea8","tjlsdhea9","tjlsdhea10","tjlsdhea11","tjlsdhea12","tjlsdhea13","tjlsdhea14","tjlsdhea15","tjlsdhea16","tjlsdhea17","tjlsdhea18","tjlsdhea19","tjlsdhea20","tjlsdhea21","tjlsdhea22","tjlsdhea23","tjlsdhea24","tjlsdhea25","tjlsdhea26","tjlsdhea27","tjlsdhea28","tjlsdhea29","tjlsdhea30","tjlsdhea31","tjlsdhea32","tjlsdhea33","tjlsdhea34","tjlsdhea35","tjlsdhea36","tjlsdhea37","tjlsdhea38","tjlsdhea39","tjlsdhea40","tjlsdhea41","tjlsdhea42","tjlsdhea43","tjlsdhea44","tjlsdhea45","tjlsdhea46","tjlsdhea47","tjlsdhea48","tjlsdhea49","tjlsdhea50","tjlsdhea51","tjlsdhea52","tjlsdhea53","tjlsdhea54","tjlsdhea55","tjlsdhea56","tjlsdhea57","tjlsdhea58","tjlsdhea59","tjlsdhea60","tjlsdhea61","tjlsdhea62","tjlsdhea63","tjlsdhea64","tjlsdhea65","tjlsdhea66","tjlsdhea67","tjlsdhea68","tjlsdhea69","tjlsdhea70","tjlsdhea71","tjlsdhea72","tjlsdhea73","tjlsdhea74","tjlsdhea75","tjlsdhea76","tjlsdhea77","tjlsdhea78","tjlsdhea79","tjlsdhea80","tjlsdhea81","tjlsdhea82","tjlsdhea83","tjlsdhea84","tjlsdhea85","tjlsdhea86","tjlsdhea87","tjlsdhea88","tjlsdhea89","tjlsdhea90","tjlsdhea91","tjlsdhea92","tjlsdhea93","tjlsdhea94","tjlsdhea95","tjlsdhea96","tjlsdhea97","tjlsdhea98","tjlsdhea99","tjlsdhea100",
    ]
    word_list += chars

    result_username = 'x' * 100 # Init username as dummy words
    while len(result_username) < size or len(result_username) >= 30: ### Limit of instagram username length is 30
        ### Case 0: Combination of words
        n_word = random.randint(1,2)
        target_word_list = list(map(lambda x: x.lower(), random.choices(word_list , k=n_word)))

        ### Case 1: Flip each word (5%)
        for word_i, target_word in enumerate(target_word_list):
            if random.random() < 0.03:
                target_word = target_word[::-1] 
            target_word_list[word_i] = target_word

        ### Case 2: replace character to 'x' or 'y' or number (3%)
        for word_i, target_word in enumerate(target_word_list):
            for ch_i in range(len(target_word)):
                if random.random() < 0.03:
                    target_char = random.choice(['x', 'y']+list(map(str, range(10))))
                    target_word = target_word[:ch_i] + target_char + target_word[ch_i+1:] 
            target_word_list[word_i] = target_word

        ### Case 3: Repeat last character (7%, 1~4 times)
        for word_i, target_word in enumerate(target_word_list):
            # if random.random() < 0.07:
            #     target_word = (target_word[0]*random.randint(1,3)) + target_word 
            if random.random() < 0.07:
                target_word += (target_word[-1]*random.randint(1,4)) 
            target_word_list[word_i] = target_word

        ### Case 4: Join the words with '.' or '_'
        joining_char = random.choice(['.', '_'])
        result_username = joining_char.join(target_word_list)

        ### Case 5: Add some number to end (30%, 1~999999)
        if random.random() < 0.3:
            if random.random() < 0.6:
                result_username += joining_char
            additional_number_list = []
            number_list = list(map(str, range(10)))
            additional_number_list.append(random.choice(number_list))
            number_list += ['']*10
            additional_number_list += random.choices(number_list, k=5)
            result_username += ''.join(list(map(str, additional_number_list)))

    return result_username

# Generating a password
def generatePassword(passwd=None):
    if passwd is None:
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(12))
    else:
        return passwd

# Generating a Email
def generatingEmail():
    return ''.join(username() + '@mail.com')

if __name__=='__main__':
    print(username(size=12, chars=string.ascii_lowercase + random.choice(['.', '_'])))
