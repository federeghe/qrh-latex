###############################################################################
# QRH Makefile.
###############################################################################
# Repository: https://github.com/federeghe/qrh-latex
# Author: Federico Reghenzani <federico §DOT§ dev §AT§ reghe §DOT§ net>
###############################################################################
#    This file is part of qrh-latex.
#
#    qrh-latex is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    qrh-latex is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with qrh-latex.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
# First of all, please configure DESTINATION variable to match your
# system directory for LaTeX packages
# Usage:
# make [all]		build the sty files
# make install		install package into the system
# make uninstall	uninstall package from the system
# make clean		clean out various auxillary files
# make test			create a pdf test using specified compiler
# make archpackage	create a package for archlinux
###############################################################################

PACKAGE = qrh

DESTINATION = /usr/share/texmf-dist/tex/latex

CP = cp
RM = rm
MKDIR = mkdir

MKTEXLSR = mktexlsr

STYFILES = qrh.sty qrhhelper.sty

LATEXCOMPILER = pdflatex -halt-on-error

all: stycheck
	$(MKDIR) -p build
	$(MKDIR) -p build/$(PACKAGE)
	$(CP) $(STYFILES) build/$(PACKAGE)

stycheck: $(STYFILES)

install: stycheck
	$(CP) -r build/$(PACKAGE) $(DESTINATION)
	$(MKTEXLSR) $(DESTINATION)/$(PACKAGE)

uninstall:
	$(RM) -r $(DESTINATION)

clean:
	$(RM) -r build
	
test:	testp180

archpackage:
	echo "Not yet implemented".

compile =									\
	$(LATEXCOMPILER) $(1) > compilation.log;				\
	if (($$?)); then							\
	  cat compilation.log;							\
	  false;								\
	fi									\

testp180:
	cd ../examples/p180 && \
	$(call compile,p180.tex)
	@echo -e "\n*** P180 compiled."
