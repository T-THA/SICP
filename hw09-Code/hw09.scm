;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  (if (= total 2) '((2) (1 1)) (if (= total 3) '((3) (2 1) (1 1 1)) '((3 1) (2 2) (2 1 1) (1 1 1 1))))
)


(define (find n lst)
  (if (= n 2) 1 0)
)


(define (find-nest n sym)
  (if (= n 1) '(car a) '(car (car (cdr a))))
)


(define-macro (def func args body)
  
)


(define-macro (k-curry fn args vals indices)
  12
)


(define-macro (let* bindings expr)
  2
)

;;; Just For Fun Problems

; Tree ADT
(define (tree label branches) (cons label branches))
(define (label t) (car t))
(define (branches t) (cdr t))
(define (is-leaf t) (null? (branches t)))

; A tree for test
(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 3 nil)
        (tree 7 (list
          (tree 7 nil)))))
    (tree 3 nil)
    (tree 6
      (list
        (tree 7 nil))))))

(define (find-in-tree t goal)
  'YOUR-CODE-HERE
)

; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  ''YOUR-CODE-HERE
)
