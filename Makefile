##
## EPITECH PROJECT, 2018
## cpp_rush3_2018
## File description:
## tests Makefile
##

NAME	=	 groundhog

SRCS	=	./groundhog.py

RM	=	rm -f

all:
	cp $(SRCS) $(NAME)

clean:
	$(RM) $(OBJS) $(OBJS:.o=.gcda) $(OBJS:.o=.gcno) $(OBJS:.o=.h.gcov)
	$(RM) $(OBJS_UT) $(OBJS_UT:.o=.gcda) $(OBJS_UT:.o=.gcno) $(OBJS_UT:.o=.h.gcov)
	$(RM) $(OBJS_UT) $(OBJS_UT:.cpp=.gcda) $(OBJS_UT:.cpp=.gcno) $(OBJS_UT:.cpp=.h.gcov)
	$(RM) $(OBJS:.o=.cpp~) $(OBJS:.o=.hpp~)
	$(RM) $(OBJS_UT:.o=.cpp~) $(OBJS_UT:.o=.hpp~)
	$(RM) *.gc*

fclean:	clean
	$(RM) $(NAME) a.out $(NAME_UT)

re:	fclean all

.PHONY:	all clean fclean re tests_run