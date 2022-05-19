#include <iostream>
#include <map>
#include <vector>
#include <string>


using namespace std;

#define SMALLBINCAP 10
#define MEDIUMBINCAP 20
#define LARGEBINCAP 30

/*class User(){  // to limit access to the list of medicines and also to verify if a user should have access to narcotics

    public:
    string userName;
    string password;
    int acccessLevel = 0; // default accessLevel is 0 : access to regular medicine but not narcotics ; accessLevel 1 = access granted to dispense narcotics

    void createUser(int userName, password){
        userName = userName;
        password = password;
    }
}

*/

class Bin{
    public:
        string size;
        int location; // location = 12 means row 1 col 2
        int currentQty; //count of medicine in the bin
    
          Bin(string x, int y, int z){
            size = x;
            location = y;
            currentQty = z;
        } 
        
        
};


class Medicine{

    public:
        int medicineID;
        string name;
        bool isNarcotic;

        Medicine(int mid, string n, bool isNarc){  //adding a new medicine to the list of medicines 
            medicineID = mid;
            name = n;
            isNarcotic = isNarc;

        }
};

class APD{ //contains methods required for the pill dispensing



    public:

        map <int, int > cabinetMedicineMap; //map of MID -> cabinet current qty  
        map <int, string> medicineID_size; //map of MIID -> size
        map <int, int> medicineID_location;  //map of MID->location

        APD ( int medID, int binQty, string Bsize, int Blocation){ //link cabinet with medicine


            cabinetMedicineMap[medID] = binQty;
            medicineID_size[medID] = Bsize;
            medicineID_location[medID] = Blocation;
            
        }

        void addPills( int mID, int qty) {//given the cabinet this method increases the count of pills in it 
            int cQty = cabinetMedicineMap[mID];
            int newQty = cQty + qty;
            cabinetMedicineMap[mID] = newQty; 

        }
        void display(Bin bin, Medicine med){
            cout << "Bin Location " << bin.location << endl;
            cout << "Bin Size" << bin.size << endl;
            cout << "MedicineID" << med.medicineID << endl;
            cout << "Medicine Name" << med.name << endl;
            cout << "Is Narcotic" << med.isNarcotic << endl;
            cout<< "Bin medicine count" << cabinetMedicineMap[med.medicineID];
        
        }

        void dispensePill(Medicine med, int qty){
            if (checkExpiry(medID)){
                cout << "Error the medicine has expired. Please refill";
            }
            else if( qty > cabinetMedicineMap[med.medicineID]){
                cout << "Error there is not enough medicine for dispensing"
            }

            int qtyCab = cabinetMedicineMap[med.medicineID];
            cabinetMedicineMap[med.medicineID] = qtyCab - qty;
            
            int binSize;

            if(medicineID_size[med.medicineID] == "small"){
                binSize = SMALLBINCAP;
            }

            if(medicineID_size[med.medicineID] == "medium"){
                binSize = MEDIUMBINCAP;
            }
            
            if(medicineID_size[med.medicineID] == "large"){
                binSize = LARGEBINCAP;
            }
        

            if (cabinetMedicineMap[med.medicineID] < (0.2 * binSize)){
                addPills(med.medicineID, 5); //add back 20% but kept it 5 for testing
            }   
            
           

        bool checkExpiry(Medicine med){ //checks if the medicine is expired; if expired returns true use #include <ctime>
            return true;
            
        }
        } 


};

int main(){
  
    Bin bin1("small", 11, 0);
    cout << "BInQTY: " << bin1.currentQty << endl;
    Medicine paracetamol(1, "paracetamol", false);  //adding a new medicine to the list of medicines 
    APD user1;
    user1.AssignMedicineCabinet( paracetamol.medicineID, bin1.currentQty); 
    user1.addPills(paracetamol.medicineID, 6);
    user1.display(bin1, paracetamol);
    return 0;

}
