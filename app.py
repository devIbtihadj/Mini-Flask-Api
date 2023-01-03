from flask import request, abort, jsonify
from models import Livre, Categorie, app
##########################################
#              GET ALL BOOKS             #
#         RECUPERER TOUS LES LIVRES      #
##########################################



@app.route('/livres', methods=['GET'])
def get_all_books():
    livres = Livre.query.order_by(Livre.id).all()
    livres_formated = [ livre.format() for livre in livres]
    if len(livres) == 0:
        abort(404)
    return jsonify({
        'success': True,
        'books': livres_formated,
        'total': len(Livre.query.all())
    })

##########################################
#          SEARCH A BOOK WITH ID         #
#       RECHERCHER UN LIVRE AVEC ID      #
##########################################
@app.route('/livres/<int:id>', methods=['GET'])
def get_one_book(id):
    try:
        livre = Livre.query.get(id)
        if livre is None:
            abort(404)
        else:
            return jsonify({
                'success' : True,
                'selected_id' : id,
                'selected_book' : livre.format()
            })
    except:
        abort(400) #BAD REQUEST

##########################################
#       LIST OF BOOKS IN A CATEGORY      #
#     LISTE DES LIVRES D'UNE CATEGORIE   #
##########################################
@app.route('/categories/<int:id>/livres', methods=['GET'])
def get_books_in_a_categorie(id):
    try:
        livres = Livre.query.filter_by(categorie_id=id).all()
        if livres is None:
            abort(404)
        else:
            livres_formated = [livre.format() for livre in livres]
            return  jsonify({
                'success' : True,
                'books' : livres_formated,
                'total' : len(livres)
            })
    except:
        abort(400) #BAD REQUEST








##########################################
#       SEARCH A CATEGORY BY ITS ID      #
#     CHERCHER UNE CATEGORIE PAR SON ID  #
##########################################
@app.route('/categories/<int:id>', methods=['GET'])
def search_a_category(id):
    try:
        categorie = Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            return jsonify({
                'success' : True,
                'selected_id' : id,
                'selected_categorie' : categorie.format()
            })
    except:
        abort(400) #BAD REQUEST


##########################################
#          LIST ALL CATEGORIES           #
#     LISTER TOUTES LES CATEGORIES       #
##########################################
@app.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Categorie.query.order_by(Categorie.id).all()
    categories_formated = [ categorie.format() for categorie in categories]
    if len(categories) == 0:
        abort(404)
    return jsonify({
        'success': True,
        'books': categories_formated,
        'total': len(Categorie.query.all())
    })

##########################################
#             DELETE A BOOK              #
#           SUPPRIMER UN LIVRE           #
##########################################
@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_one_book(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        livre.delete()
        return jsonify({
            'success': True,
            'deleted_id': id,
            'deleted_book': livre.format(),
            'total': Livre.query.count()
        })

##########################################
#           DELETE A CATEGORY            #
#         SUPPRIMER UNE CATAGORIE        #
##########################################
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_a_category(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        categorie.delete()
        return jsonify({
            'success': True,
            'deleted_id': id,
            'deleted_category': categorie.format(),
            'total': Livre.query.count()
        })

##########################################
#        EDIT BOOK INFORMATION           #
#  MODIFIER LES INFORMATIONS D'UN LIVRE  #
##########################################
@app.route('/livres/<int:id>', methods=['PATCH'])
def update_a_book(id):
    livre = Livre.query.get(id)
    body = request.get_json()
    livre.isbn = body.get('isbn', None)
    livre.titre = body.get('titre', None)
    livre.date_publication = body.get('date_publication', None)
    livre.auteur = body.get('auteur', None)
    livre.editeur = body.get('editeur', None)
    livre.categorie_id = body.get('categorie_id', None)
    if livre.isbn is None or livre.titre is None or livre.date_publication is None or livre.auteur is None or livre.editeur is None or livre.categorie_id is None:
        abort(400)
    else:
        livre.update()
        return jsonify({
            'success': True,
            'updated_book_id': id,
            'new_book': livre.format()
        })

##########################################
#    MODIFY THE LABEL OF A CATEGORY      #
#  MODIFIER LE LIBELLE D'UNE CATEGORIE   #
##########################################
@app.route('/categories/<int:id>', methods=['PATCH'])
def update_a_category(id):
    category = Categorie.query.get(id)
    body = request.get_json()
    category.libelle_categorie = body.get('libelle_categorie', None)
    if body.libelle_categorie is None:
        abort(400)
    else:
        category.update()
        return jsonify({
            'success': True,
            'updated_category_id': id,
            'new_category': category.format()
        })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success" :False,
        "error" : 404,
        "message" : "Not found"
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
    }), 400