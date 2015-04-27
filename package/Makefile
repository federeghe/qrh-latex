###############################################################################
# QRH Makefile.
###############################################################################
# LICENSE: GNU Lesser General Public License 3
# Repository: https://github.com/federeghe/qrh-latex
# Author: Federico Reghenzani <federico §DOT§ dev §AT§ reghe §DOT§ net>
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
