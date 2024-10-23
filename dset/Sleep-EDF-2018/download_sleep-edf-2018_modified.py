import os
import requests

# Ensure the destination directory exists
os.makedirs('./edf', exist_ok=True)

urls = [
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4001E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4001EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4002E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4002EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4011E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4011EH-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4012E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4012EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4021E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4021EH-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4022E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4022EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4031E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4031EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4032E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4032EP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4041E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4041EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4042E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4042EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4051E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4051EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4052E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4052EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4061E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4061EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4062E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4062EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4071E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4071EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4072E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4072EH-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4081E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4081EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4082E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4082EP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4091E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4091EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4092E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4092EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4101E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4101EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4102E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4102EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4111E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4111EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4112E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4112EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4121E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4121EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4122E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4122EV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4131E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4131EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4141E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4141EU-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4142E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4142EU-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4151E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4151EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4152E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4152EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4161E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4161EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4162E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4162EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4171E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4171EU-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4172E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4172EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4181E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4181EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4182E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4182EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4191E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4191EP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4192E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4192EV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4201E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4201EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4202E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4202EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4211E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4211EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4212E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4212EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4221E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4221EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4222E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4222EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4231E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4231EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4232E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4232EV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4241E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4241EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4242E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4242EA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4251E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4251EP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4252E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4252EU-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4261F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4261FM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4262F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4262FC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4271F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4271FC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4272F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4272FM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4281G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4281GC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4282G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4282GC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4291G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4291GA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4292G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4292GC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4301E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4301EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4302E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4302EV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4311E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4311EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4312E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4312EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4321E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4321EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4322E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4322EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4331F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4331FV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4332F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4332FC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4341F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4341FA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4342F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4342FA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4351F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4351FA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4352F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4352FV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4362F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4362FC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4371F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4371FA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4372F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4372FC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4381F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4381FC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4382F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4382FW-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4401E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4401EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4402E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4402EW-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4411E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4411EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4412E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4412EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4421E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4421EA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4422E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4422EA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4431E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4431EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4432E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4432EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4441E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4441EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4442E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4442EV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4451F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4451FY-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4452F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4452FW-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4461F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4461FA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4462F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4462FJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4471F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4471FA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4472F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4472FA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4481F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4481FV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4482F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4482FJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4491G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4491GJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4492G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4492GJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4501E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4501EW-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4502E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4502EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4511E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4511EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4512E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4512EW-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4522E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4522EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4531E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4531EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4532E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4532EV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4541F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4541FA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4542F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4542FW-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4551F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4551FC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4552F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4552FW-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4561F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4561FJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4562F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4562FJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4571F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4571FV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4572F0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4572FC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4581G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4581GM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4582G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4582GP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4591G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4591GY-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4592G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4592GY-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4601E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4601EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4602E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4602EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4611E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4611EG-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4612E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4612EA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4621E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4621EV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4622E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4622EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4631E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4631EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4632E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4632EA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4641E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4641EP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4642E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4642EP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4651E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4651EP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4652E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4652EG-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4661E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4661EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4662E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4662EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4671G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4671GJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4672G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4672GV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4701E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4701EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4702E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4702EA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4711E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4711EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4712E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4712EA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4721E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4721EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4722E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4722EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4731E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4731EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4732E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4732EJ-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4741E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4741EA-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4742E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4742EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4751E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4751EC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4752E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4752EM-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4761E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4761EP-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4762E0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4762EG-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4771G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4771GC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4772G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4772GC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4801G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4801GC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4802G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4802GV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4811G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4811GG-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4812G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4812GV-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4821G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4821GC-Hypnogram.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4822G0-PSG.edf',
'https://www.physionet.org/physiobank/database/sleep-edfx/sleep-cassette/SC4822GC-Hypnogram.edf'
]


# Function to download files using requests
def download_file(url, destination_folder):
    local_filename = url.split('/')[-1]
    local_filepath = os.path.join(destination_folder, local_filename)

    # Make the request to download the file
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()  # Check for HTTP errors
            # Write the content to a local file in chunks
            with open(local_filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive chunks
                        f.write(chunk)
        print(f"Downloaded {local_filename} to {destination_folder}")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh} - {url}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc} - {url}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt} - {url}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err} - {url}")

# Download each file
i = 0
for url in urls:
    i = i+1
    print(f"{i} of {len(urls)}")
    download_file(url, './edf')