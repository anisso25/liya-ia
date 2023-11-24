from bardapi import Bard
import os

# Replace XXXX with the correct value ending with a dot
os.environ['_BARD_API_KEY'] = "dQhlzNyfABV4NeSaFTpQASNPM8c_YJ7x4f9Jed9tQDVFsYYVAmbNDbvfrjJJqii-a4dcPw."

# Replace YYYYY with the correct value for SNlM0e
snim0e_value = "YYYYY"

# Pass both values explicitly
bard = Bard(token=os.environ['_BARD_API_KEY'], snim0e=snim0e_value)
# Rest of your code...
