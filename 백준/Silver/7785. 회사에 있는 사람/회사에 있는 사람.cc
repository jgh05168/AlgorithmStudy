#include <iostream>
#include <string>
#include <map>

using namespace std;

int n;
map<string, int, greater<string>> company_log;

int main() {
	cin >> n;
	string name, state;
	while (n--) {
		cin >> name >> state;
		if (!company_log[name] && state == "enter")
			company_log[name] = 1;
		else if (company_log[name] && state == "leave")
			company_log.erase(name);
	}

	for (auto name : company_log) {
		cout << name.first << '\n';
	}

	return 0;
}