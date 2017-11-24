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

(define (pascals-triangle n)
  ;;; Display an inverted version of Pascal's triangle starting
  ;;; at row `n`
  (define (build-triangle n count)
    (if (= count n)
        (binom-coef count)
        (string-append (binom-coef count)
                       "\n"
                       (build-triangle n (+ count 1)))))
  (display (build-triangle n 1)))


