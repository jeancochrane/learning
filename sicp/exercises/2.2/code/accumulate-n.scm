(load "/home/jean/learning/sicp/exercises/2.2/code/accumulate.scm")

(define (accumulate-n op init seqs)
  ;;; Apply the operator `op` to a sequence of sequences, `seqs`, such that
  ;;; the elements of each sequence at a given index are accumulated
  (if (null? (car seqs))
      (list)
      (cons (accumulate op init (map car seqs))
            (accumulate-n op init (map cdr seqs)))))

;;; Test
(accumulate-n + 0 (list (list 1 2 3) (list 4 5 6) (list 7 8 9) (list 10 11 12)))
;;; Expected: (22 26 30)
