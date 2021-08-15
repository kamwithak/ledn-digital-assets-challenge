
accounts = {}
def getListOfUniqueCountries():
  unique_list_of_country_codes = {}
  key_country = 0
  for account in accounts:
    country = account['Country']
    if (country not in unique_list_of_country_codes.values()):
      unique_list_of_country_codes[key_country] = country
      key_country += 1
  return unique_list_of_country_codes


def getListOfUniqueMFAs():
  unique_list_of_mfa_types = {}
  key_mfa = 0
  for account in accounts:
    mfa = account['mfa']
    if (mfa not in unique_list_of_mfa_types.values()):
      unique_list_of_mfa_types[key_mfa] = mfa
      key_mfa += 1
  return unique_list_of_mfa_types

print("List of Countries:")
print(getListOfUniqueCountries())
print("List of MFA Types:")
print(getListOfUniqueMFAs())