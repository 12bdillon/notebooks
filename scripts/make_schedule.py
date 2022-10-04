import glob
import re
github_organization = "CMPS-6100"
github_repo = "notebooks"
def get_header(fname):
	try:
		return re.sub('#', '', open(fname).readlines()[0]).strip()
	except Exception as e:
		return 'name'

for module in sorted(glob.glob("[0-9][0-1]-*")):
	module_title = '**{}**'.format(get_header('{}/README.md'.format(module)))
	print('|[{}](https://github.com/{}/{}/tree/main/{})|'.format(module_title, github_organization, github_repo, module))
	for lecture in sorted(glob.glob('{}/0*'.format(module))):
		lecture_title = "{}".format(lecture.split('/')[1][3:-6].capitalize())
		ipynb = '&nbsp;&nbsp;[{}](https://nbviewer.jupyter.org/github/{}/{}/blob/main/{}?flush_cache=True)'.format(lecture_title, github_organization, github_repo, lecture)

		print('|{}|'.format(ipynb))
