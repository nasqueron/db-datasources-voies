RM=rm -f

all: fantoir-doc/nature_voie.json

fantoir-doc/nature_voie.json: fantoir-doc/nature_voie.dat
	utils/parse-kv-spaces.py fantoir-doc/nature_voie.dat > fantoir-doc/nature_voie.json

clean:
	${RM} fantoir-doc/nature_voie.json
