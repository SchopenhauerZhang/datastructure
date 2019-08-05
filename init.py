import subprocess


def init():
	try:
		subprocess.call("python --version", shell = True)
	except Exception:
		exit("sorry ,your python env is not available")


if __name__ == "__main__":
	init()

