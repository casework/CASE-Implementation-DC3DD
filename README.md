# DC3DD Python-Embedded-in-C Prototype

Note that this prototype is not complete and was abandoned for the wrapper-prototype.
However, it is included so that at least some of the work in an approach involving
embedding Python in C will not have to begin without some ground work.


# CLI Wrapper Prototype

This is a proof-of-concept (POC) that started out with a need to represent information from DC3DD in CASE format.

During discussions with the current maintainer it was established that the tool is meant to be easy, fast, and lightweght.
Thus, the initial idea of embedding Python into the C codebase was scrapped and a CLI wrapper written instead.
The CLI wrapper would grab the configuration flags of the tool, the only real settings/output from the tool,
other than console output and the actual copied raw image (both inappropriate to represent in CASE format).

As the wrapper was developed it was decided it would be nice for analysts to be abel to input some information.
Some of this was done via the bash script to prompt the user (this could be a GUI but for this tool this is not in scope),
while a text file was introduced as another means of ingestion, one that allows more granular control.
The process of ingesting this information can be referred to as translation, and is performed by the translator.py file.

The translator relies on a converter (converter.py), which does a basic transformation of the encapsulation and inheritance
that the user wishes to represent via the config-format.txt file's description, as well as transformation of the values
from strings to the code's datatypes (in this case, strings to Pythonic str, bool, int, and datetime objects).

A mapping file is used to illustrate how a direct mapping file can be used to map a tool field to a CASE field.
Obviously, this example is not comprehensive as this POC unintentionally evolved into illustrating several ideas.

Future ideas involve: adding GUI/easier interface for manual ingestion, an update to CASE version past v0.1.0, and the possible move towards this being a easily imported library to support small tool developers on GitHub who would like to express investigative metadata along with their tool output, enabling ingest into larger household names like Autopsy.

### How to run:

./wrapper dc3dd if=some-file of=some-file


### Output files:

The test_dc3dd.json file contains the CASE JSON-LD output.
The tmp_out.txt file shows the bash-scraped CLI info.


### Other information:

See the dc3dd.config.failexample file for an improperly formatted config file.


# I have a question!

Before you post a Github issue or send an email ensure you've done this checklist:

1. [Determined scope](https://caseontology.org/ontology/start.html#scope) of your task. It is not necessary for most parties to understand all aspects of the ontology, mapping methods, and supporting tools.

2. Familiarize yourself with the [labels](https://github.com/casework/CASE-CLI-Wrapper/labels) and search the [Issues tab](https://github.com/casework/CASE-CLI-Wrapper/issues). Typically, only light-blue and red labels should be used by non-admin Github users while the others should be used by CASE Github admins.
*All but the red `Project` labels are found in every [`casework`](https://github.com/casework) repository.*
