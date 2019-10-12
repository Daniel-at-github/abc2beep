# abc2beep

Converts [abc music notation](http://abcnotation.com/) text file to a commandline [beep](https://linux.die.net/man/1/beep) script (pcspkr music)

## Usage

~~~ bash
abc2beep.py examples/speed_the_plough.abc | tee examples/speed_the_plough.sh

wget https://sites.google.com/site/lotroabc/n3.abc -O examples/always_look_on_the_bright_side_of_life.abc
abc2beep.py examples/always_look_on_the_bright_side_of_life.abc 240 | bash
~~~

## Example

### Input

~~~ abc
X:1
T:Speed the Plough
M:4/4
C:Trad.
K:G
|:GABc dedB|dedB dedB|c2ec B2dB|c2A2 A2BA|
  GABc dedB|dedB dedB|c2ec B2dB|A2F2 G4:|
|:g2gf gdBd|g2f2 e2d2|c2ec B2dB|c2A2 A2df|
  g2gf g2Bd|g2f2 e2d2|c2ec B2dB|A2F2 G4:|
~~~

### Output

~~~ bash
beep \
  --new -f   392.00 -l   175.00 -D     0.00 \
  --new -f   440.00 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   350.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   350.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   350.00 -D     0.00 \
  --new -f   440.00 -l   350.00 -D     0.00 \
  --new -f   440.00 -l   350.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   440.00 -l   175.00 -D     0.00 \
  --new -f   392.00 -l   175.00 -D     0.00 \
  --new -f   440.00 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   350.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   350.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   440.00 -l   350.00 -D     0.00 \
  --new -f   369.99 -l   350.00 -D     0.00 \
  --new -f   392.00 -l   700.00 -D     0.00 \
  --new -f   783.99 -l   350.00 -D     0.00 \
  --new -f   783.99 -l   175.00 -D     0.00 \
  --new -f   739.99 -l   175.00 -D     0.00 \
  --new -f   783.99 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   783.99 -l   350.00 -D     0.00 \
  --new -f   739.99 -l   350.00 -D     0.00 \
  --new -f   659.26 -l   350.00 -D     0.00 \
  --new -f   587.33 -l   350.00 -D     0.00 \
  --new -f   523.25 -l   350.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   350.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   350.00 -D     0.00 \
  --new -f   440.00 -l   350.00 -D     0.00 \
  --new -f   440.00 -l   350.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   739.99 -l   175.00 -D     0.00 \
  --new -f   783.99 -l   350.00 -D     0.00 \
  --new -f   783.99 -l   175.00 -D     0.00 \
  --new -f   739.99 -l   175.00 -D     0.00 \
  --new -f   783.99 -l   350.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   783.99 -l   350.00 -D     0.00 \
  --new -f   739.99 -l   350.00 -D     0.00 \
  --new -f   659.26 -l   350.00 -D     0.00 \
  --new -f   587.33 -l   350.00 -D     0.00 \
  --new -f   523.25 -l   350.00 -D     0.00 \
  --new -f   659.26 -l   175.00 -D     0.00 \
  --new -f   523.25 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   350.00 -D     0.00 \
  --new -f   587.33 -l   175.00 -D     0.00 \
  --new -f   493.88 -l   175.00 -D     0.00 \
  --new -f   440.00 -l   350.00 -D     0.00 \
  --new -f   369.99 -l   350.00 -D     0.00 \
  --new -f   392.00 -l   700.00 -D     0.00
~~~

## Resources

* abcnotation tunes: https://abcnotation.com/tunes
* Shared online editor with [abcnotation rendering feature](https://hackmd.io/features?both#Abc):
  * Online: https://hackmd.io
  * Self hosted: https://github.com/hackmdio/codimd
