(define (pascals-triangle n)
  ;;; Compute and display Pascal's triangle up to row `n`
  (define (pascal row col)
    ;;; Calculate a value in Pascal's triangle for a given row and col
    (cond ((or (= col 1) (= row col)) 1)  ; Edges of the triangle
          ((or (< col 1) (> col row)) 0)  ; Ignore values beyond triangle bounds
          (else (+ (pascal (- row 1) (- col 1))  ; Preceding value on the left
                   (pascal (- row 1) col)))))    ; Preceding value on the right
  (define (binom-coef n)
    ;;; Display the binomial coefficients for `n`
    (define (pascal-row row col)
        (if (= row col)
            (write-to-string (pascal row col))
            (string-append (write-to-string (pascal row col))
                            " "
                            (pascal-row row (+ col 1)))))
    (pascal-row n 1))
  (define (build-triangle n count)
    (if (= count n)
        (binom-coef count)
        (string-append (binom-coef count)
                       "\n"
                       (build-triangle n (+ count 1)))))
  (display (build-triangle n 1)))

(define (pascal-iter n)
  ;;; Compute and display Pascal's triangle up to row `n` -- iteratively!
  (define (list-to-string str lst)
    (if (null? (cdr lst))
        str
        (list-to-string (string-append str " " (car lst)) (cdr lst))))
  (define (next-row curr-coefs row)
    (if (null? (cdr row))
        (append curr-coefs (list (car row))) ; Make sure to append the trailing 0
        (next-row (append curr-coefs (list (+ (car row) (cadr row))))
                  (cdr row))))
  (define (build-triangle str lst n count)
    (let (next-str (string-append str "\n" (list-to-string "" (next-row (list) lst)))
      (if (= count n)
          next-str
          (build-triangle next-str (next-row (list) lst) n (+ count 1))))))
  (let (init-value (list 0 1 0))
    (display (build-triangle (list-to-string "" init-value) init-value n 1))))
