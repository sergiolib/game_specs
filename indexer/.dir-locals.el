;;; Directory Local Variables            -*- no-byte-compile: t -*-
;;; For more information see (info "(emacs) Directory Variables")

((nil . ((db-user . "postgres")
	 (db-password . "123")
	 (db-name . "postgres")
	 (db-host . "localhost")
	 (db-port . "5433")
	 (eval . (setq-local compile-command (concat "cd game_specs/ && poetry run python indexer/main.py " db-host " " db-user " " db-password " " db-name " " db-port))))))
